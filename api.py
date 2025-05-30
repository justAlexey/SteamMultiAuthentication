steam_guard_code_len = 26

steam_guard_code_translations = [
    50, #0
    51, #1
    52, #2
    53, #3
    54, #4
    55, #5
    56,
    57,
    66,
    67,
    68, #10
    70,
    71,
    72,
    74,
    75, #15
    77,
    78,
    80,
    81,
    82, #20
    84,
    86,
    87,
    88,
    89 #25
]

class API_Endpoints:
    ADD_AUTH = "https://api.steampowered.com/ITwoFactorService/AddAuthenticator/v1/?access_token="
    FINALIZE_ADD_AUTH = "https://api.steampowered.com/ITwoFactorService/FinalizeAddAuthenticator/v1/?access_token="
    GET_USER_COUNTRY = "https://api.steampowered.com/IUserAccountService/GetUserCountry/v1?access_token="
    GET_ACCOUNT_PHONE_STATUS = "https://api.steampowered.com/IPhoneService/AccountPhoneStatus/v1?access_token="
    SET_ACCOUNT_PHONE_NUMBER = "https://api.steampowered.com/IPhoneService/SetAccountPhoneNumber/v1?access_token="
    VERIFY_PHONE_WITH_CODE = "https://api.steampowered.com/IPhoneService/VerifyAccountPhoneWithCode/v1/?access_token="
    IS_ACCOUNT_WAITING_FOR_EMAIL_CONFIRMATION = "https://api.steampowered.com/IPhoneService/IsAccountWaitingForEmailConfirmation/v1?access_token="
    SEND_PHONE_VERIFICATION_CODE = "https://api.steampowered.com/IPhoneService/SendPhoneVerificationCode/v1?access_token="
    REFRESH_ACCESS_TOKEN = "https://api.steampowered.com/IAuthenticationService/GenerateAccessTokenForApp/v1/"
    TWO_FACTOR_TIME_QUERY = "https://api.steampowered.com/ITwoFactorService/QueryTime/v0001"