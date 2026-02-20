import pytest

from Capstone_Project.conftest import logger
from Capstone_Project.pages.Remove_Product import RemoveProduct

@pytest.mark.order(5)
def test_remove_product(setup):
    logger.info("========== STARTING REMOVE PRODUCT TEST ==========")
    driver = setup
    cart_page = RemoveProduct(driver)

    # Go to shop and add product
    logger.info("Navigating to Shop page")
    cart_page.go_to_shop()
    current_url = driver.current_url
    logger.info(f"Current URL after navigation: {current_url}")
    assert "shop" in driver.current_url.lower(), (
        f"Shop page did not open.\n"
        f"Current URL: {driver.current_url}"
    )
    logger.info("Adding product to basket")
    cart_page.add_product_to_basket()
    logger.info("Validating View Basket button visibility")
    view_basket_btn = driver.find_element(*cart_page.view_basket)
    assert view_basket_btn.is_displayed(), "Add to Basket button click failed"
    logger.info("Clicking View Basket button")
    cart_page.click_view_basket()
    logger.info(f"Current URL after clicking View Basket: {driver.current_url}")
    assert "basket" in driver.current_url.lower(), "View Basket button click failed"

    # Remove first product
    logger.info("Removing product from cart")
    cart_page.remove_product_from_cart()
    remaining_products = driver.find_elements(*cart_page.remove_btn)
    logger.info(f"Remaining remove buttons count: {len(remaining_products)}")
    assert not driver.find_elements(*cart_page.remove_btn), "Remove button click failed"

    # Optional: check cart is empty or product removed
    final_url = cart_page.get_current_url()
    assert "basket" in cart_page.get_current_url()
    logger.info(f"Final URL after removal: {final_url}")
    logger.info("========== REMOVE PRODUCT TEST PASSED ==========")
