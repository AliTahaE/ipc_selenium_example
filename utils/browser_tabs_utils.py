
def switch_to_new_tab(driver, current_tab_handle, tabs_handles):
    for handle in tabs_handles:
        if handle != current_tab_handle:
            driver.switch_to.window(handle)


def switch_to_default_screen(driver, default_window):
    driver.switch_to.window(default_window)
