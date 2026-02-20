import pytest

from Capstone_Project.conftest import logger
from Capstone_Project.pages.Add_Product import AddProduct

@pytest.mark.order(4)
def test_add_product_to_cart(setup):
    logger.info("========== STARTING ADD PRODUCT TO CART TEST ==========")
    driver = setup
    product = AddProduct(driver)

    # Step 1: Go to Shop
    logger.info("Navigating to Shop page")
    product.go_to_shop()
    assert "shop" in driver.current_url.lower(), (
        f"Shop page did not open.\n"
        f"Current URL: {driver.current_url}"
    )

    # Step 2: Add product to basket
    logger.info(f"Current URL after navigation: {driver.current_url}")
    logger.info("Adding product to basket")
    product.add_product_to_basket()
    logger.info("Validating product added to basket (View Basket visible)")
    view_basket_visible = driver.find_elements(*product.add_basket_btn)
    assert len(view_basket_visible) > 0, "Product was not added to the basket (View Basket not visible)."
    logger.info("View basket button clicked")
    # Step 3: Click View Basket
    product.click_view_basket()

    # -------- Assertions --------
    logger.info("Validating basket page URL")
    assert "basket" in product.get_current_url().lower()
    logger.info("Validating page title")
    logger.info(f"Page title: {driver.title}")
    assert driver.title == "Basket – Automation Practice Site"
    logger.info("========== ADD PRODUCT TO CART TEST PASSED ==========")