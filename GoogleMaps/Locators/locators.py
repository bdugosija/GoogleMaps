class Locators:

    search_textbox_id = 'searchboxinput'
    search_button_id = 'searchbox-searchbutton'
    get_directions_button_id = 'searchbox-directions'
    directions_inputbox1_xpath = "//div[@id='sb_ifc51']/input"
    directions_inputbox2_xpath = "//div[@id='sb_ifc52']/input"
    car_button_xpath = "//div[@class='adjusted-to-decreased-spacing directions-travel-mode-selector']/div[2]/button"
    options_button_xpath = "//button[@class=' section-directions-options-link']"
    avoid_highways_checkbox_xpath = "//label[@for='pane.directions-options-avoid-highways']"
    all_routes_xpath = "//div[@class='section-listbox']//div[@class='section-directions-trip-distance section-directions-trip-secondary-text']"
    details_button_xpath = "//div[@class='section-directions-trip clearfix selected']//button[@class='section-directions-trip-details-link noprint blue-button-text']"
    #details_duration_xpath = "//h1[@class='section-trip-summary-title']//span[@class='delay-light']"
    details_duration_xpath = "//h1[@class='section-trip-summary-title']/span/span"
    details_distance_xpath = "//h1[@class='section-trip-summary-title']//span[@class='section-trip-summary-subtitle']/span"
    menu_button_xpath = "//button[@class='searchbox-hamburger white-foreground']"
    language_button_xpath = "//button[@class='widget-languages-drawer-button widget-settings-button']"