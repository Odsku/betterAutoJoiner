from twocaptcha import TwoCaptcha, api

class Captcha:
    APIKey = None

    # Error Handler #
    # Messy error handler but it does the job # 
    def ErrorHandler(self, error):
        error = error.__str__()

        if error == "ERROR_WRONG_USER_KEY":
            return True, "You've provided key parameter value in incorrect format, it should contain 32 symbols."
        elif error == "ERROR_KEY_DOES_NOT_EXIST":
            return True, "The key you've provided does not exists."
        elif error == "ERROR_ZERO_BALANCE":
            return True, "You don't have funds on your account."
        elif error == "ERROR_PAGEURL":
            return True, "'pageurl' parameter is missing in your request."
        else:
            return False, f"Unknown error ({error})"

    # Get balance #
    def Balance(self):
        solver = TwoCaptcha(self.APIKey)
        try:
            result = solver.balance()
        except api.ApiException as e:
            should_exit, message = self.ErrorHandler(e)
            print(message)
            if should_exit:
                quit()
            return 0.00
        except Exception as e:
            print(e)
            return 0.00
        else:
            return result

    # Solve captcha #
    def Solve(self):
        solver = TwoCaptcha(self.APIKey)

        try:
            result = solver.hcaptcha(
                sitekey="30a8dcf5-481e-40d1-88de-51ad22aa8e97",
                url="https://rblxwild.com",
            )

        except api.ApiException as e:
            should_exit, message = self.ErrorHandler(e)
            print(message)
            if should_exit:
                quit()
            return False

        except Exception as e:
            print(e)
            return False
        else:
            return result

# Copyright © 2022 Odsku. All rights reserved.