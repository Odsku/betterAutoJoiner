from twocaptcha import TwoCaptcha

class Captcha:
    APIKey = None

    def Balance(self):
        solver = TwoCaptcha(self.APIKey)
        return solver.balance()

    # Solve captcha #
    def Solve(self):
        solver = TwoCaptcha(self.APIKey)

        try:
            result = solver.hcaptcha(
                sitekey="30a8dcf5-481e-40d1-88de-51ad22aa8e97",
                url="https://rblxwild.com",
            )

        except Exception as e:
            print(e)
            return False
        else:
            return result