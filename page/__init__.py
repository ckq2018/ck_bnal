from selenium.webdriver.common.by import By

# 以下是百年奥莱登录数据
loc_my = By.ID, "com.yunmall.lc:id/tab_me"
loc_logins = By.ID, "com.yunmall.lc:id/textView1"
loc_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
loc_password = By.ID, "com.yunmall.lc:id/logon_password_textview"
loc_login = By.ID, "com.yunmall.lc:id/logon_button"
loc_login_nick = By.ID, "com.yunmall.lc:id/tv_user_nikename"
loc_click_set = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
loc_sms = By.ID, "com.yunmall.lc:id/setting_sms_notify"
loc_update_pwd = By.ID, "com.yunmall.lc:id/setting_modify_pwd"
loc_exit = By.ID, "com.yunmall.lc:id/setting_logout"
loc_is_exit = By.ID, "com.yunmall.lc:id/ymdialog_right_button"


"""以下数据为 百年奥莱地址管理配置数据"""
# 地址管理
address_manage = By.ID,"com.yunmall.lc:id/setting_address_manage"
# 新增地址
address_add_new_btn = By.ID, "com.yunmall.lc:id/address_add_new_btn"
# 收件人
address_receipt_name = By.ID , "com.yunmall.lc:id/address_receipt_name"
# 电话
address_add_phone = By.ID, "com.yunmall.lc:id/address_add_phone"
# 所在区域
address_area = By.ID, "com.yunmall.lc:id/address_province"
# 省  id重复 只能使用text

# 市  class = "android.widget.RelativeLayout"
shi = By.ID ,"com.yunmall.lc:id/area_title"
# 区 使用 text

# 输入详细地址
address_detail_addr_info = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
# 输入邮编
address_post_code = By.ID, "com.yunmall.lc:id/address_post_code"
# 设为默认地址
address_default = By.ID, "com.yunmall.lc:id/address_default"
# 保存
address_save = By.ID, "com.yunmall.lc:id/button_send"
# 获取所有的收件人和电话 (id都是一样)
receipt_name = By.ID, "com.yunmall.lc:id/receipt_name"
