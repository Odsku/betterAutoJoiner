import time, requests

def LoadFromArray(array):
    sessions = []
    for acc in array:
        new_session = RBLXWild()
        new_session.username = acc["username"]
        new_session.authToken = acc["authToken"]
        new_session.session = acc["session"]
        new_session.useragent = acc["useragent"]

        sessions.append(new_session)
    
    return sessions

class RBLXWild:
    username = None
    authToken = None
    session = None
    useragent = None


    # Join pot #
    def Join(self, potId, captchaToken):
        # Header data #
        headers = {
            "User-Agent": self.useragent,
            "Accept-Language": "en-US,en;q=0.5",
            "Authorization": self.authToken,
            "Origin": "https://rblxwild.com",
            "DNT": "1",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "TE": "trailers"
    }

        # Cookie data #
        cookies = {
            "session": self.session
        }

        # Post data #
        json = {
            "captchaToken": captchaToken, 
            "potId": potId, 
            "i1oveu": True
        }

        try:
            response = requests.post("https://rblxwild.com/api/events/rain/join", json=json, headers=headers, cookies=cookies)
        except Exception as e:
            print(e)
            return False
        else:
            return response