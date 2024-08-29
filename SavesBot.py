from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.common.exceptions import NoSuchElementException

from time import sleep
import datetime
import os
import logging

class InstaSavesBot():
    def __init__(self, username, password, mensagem):

        # Configurações Chrome
        ChromeOptions = webdriver.ChromeOptions()
        ChromeOptions.add_argument("--incognito")
        ChromeOptions.add_argument("--headless")

        # Configurações do log
        hora = datetime.datetime.now()
        pasta_alvo = "logs/"
        if(not os.path.exists(pasta_alvo)):
            os.mkdir(pasta_alvo)
        logging.basicConfig(
            level=logging.INFO,
            format=" [%(asctime)s] [%(filename)s] [%(lineno)d] %(message)s",
            filename=f"./logs/{str(datetime.date.today())}-{str(hora.hour)}-{str(hora.minute)}-{str(hora.second)}"
            )

        self.username = username
        self.password = password
        self.mensagem = mensagem
        self.driver = webdriver.Chrome(ChromeOptions)
        self.profile_list = []
        self.enviados = []
        self.nao_enviados = []
    def login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.instagram.com/')
        sleep(2)
        print("REALIZANDO ACESSO A CONTA")
        logging.info("REALIZANDO ACESSO A CONTA")
        try:
            username_element = driver.find_element(By.NAME, 'username')
            username_element.clear()
            sleep(0.5)
            username_element.send_keys(self.username)
            sleep(0.5)
            password_element = driver.find_element(By.NAME, 'password')
            password_element.clear()
            sleep(0.5)
            password_element.send_keys(self.password)
            sleep(0.5)
            password_element.send_keys(Keys.RETURN)
            sleep(5)
            print(f'ACESSO REALIZADO COM SUCESSO')
            logging.info("ACESSO REALIZADO COM SUCESSO")
        except:
            logging.critical("ERRO AO ACESSAR")
            return print("ERRO AO ACESSAR")
        
        self.AcessaSalvos()
    def AcessaSalvos(self):
        driver = self.driver
        driver.get(f'https://www.instagram.com/{self.username}/saved/all-posts/')
        print("ACESSANDO TODOS OS SALVOS")
        logging.info("ACESSANDO TODOS OS SALVOS")
        sleep(3)
        self.ListarPerfis()    
    def ListarPerfis(self):
        driver = self.driver
        posts_linha = len(driver.find_elements(By.XPATH, "//div[contains(@class, '_ac7v') and contains(@class, '_al3n')]"))
        print("INICIANDO LISTAGEM DE PERFIS...")
        logging.info("INICIANDO LISTAGEM DE PERFIS...")
        if(posts_linha > 8):
            posts_linha == 8
        for l in range(1, posts_linha, 1):
            for x in range(1, 4, 1):
                post_element = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div[3]/article/div[1]/div/div[{l}]/div[{x}]/a')
                driver.execute_script('arguments[0].click();', post_element)
                sleep(1)
                profile_element = "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div._ae65 > div > div > div._aasi > div > header > div._aaqy._aaqz > div._aar0._aar1 > div > div > div > span > span > div > a"
                try:
                    profile_name = driver.find_element(By.CSS_SELECTOR, profile_element)
                    print("ELEMENTO LOCALIZADO POR CSS SELECTOR")
                    logging.info("ELEMENTO LOCALIZADO POR CSS SELECTOR")
                except:
                    try:
                        profile_element = "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div/div/div/span/span/div/a"    
                        profile_name = driver.find_element(By.XPATH, profile_element)
                        print("ELEMENTO LOCALIZADO POR XPATH")
                        logging.info("ELEMENTO LOCALIZADO POR XPATH")
                    except:
                        try:
                            profile_element = "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div._ae65 > div > div > div._aasi > div > header > div._aaqy._aaqz > div._aar0._aar1 > div > div > span > span:nth-child(1) > div > a"
                            profile_name = driver.find_element(By.CSS_SELECTOR, profile_element)
                            print("ELEMENTO LOCALIZADO POR CSS SELECTOR")
                            logging.info("ELEMENTO LOCALIZADO POR CSS SELECTOR")
                        except:
                            try:
                                profile_element = "/html/body/div[8]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div/div/span/span[1]/div/a"
                                profile_name = driver.find_element(By.CSS_SELECTOR, profile_element)
                                print("ELEMENTO LOCALIZADO POR XPATH")
                                logging.info("ELEMENTO LOCALIZADO POR XPATH")
                            except:
                                logging.critical("ELEMENTO NÃO LOCALIZADO")
                                return print("ELEMENTO NÃO LOCALIZADO")

                self.AdicionaPerfil(profile_name.text)     
                self.RetiraSalvo(profile_name.text)
        print("LISTAGEM DE PERFIS FINALIZADA!")
        logging.info("LISTAGEM DE PERFIS FINALIZADA!")
        self.AcessaPerfis()
    def FecharNotificacao(self):
        driver = self.driver
        sleep(5)
        notification_element = "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"
        try:
            notification_close = driver.find_element(By.XPATH, notification_element)
        except:
            try:
                notification_element = "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._ap36._a9_1"
                notification_close = driver.find_element(By.CSS_SELECTOR, notification_element)
            except Exception:
                sleep(5)
                logging.critical("ERRO AO FECHAR NOTIFICAÇÃO")
                return print("ERRO AO FECHAR NOTIFICAÇÃO")
            
        notification_close.click()
        print("NOTIFICAÇÃO FECHADA COM SUCESSO")
        logging.info("NOTIFICAÇÃO FECHADA COM SUCESSO")
    def EnviaMsg(self, p):
        driver = self.driver
        sleep(2)
        input_element = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]"
        try:
            mensagem_element = driver.find_element(By.XPATH, input_element)
        except:
            try:
                input_element = '#mount_0_0_UG > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x1v4esvl > section > div > div > div > div.xjp7ctv > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x193iq5w.xeuugli.x1r8uery.x1iyjqo2.xs83m0k > div > div > div > div > div > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div:nth-child(2) > div > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1i64zmx.xw3qccf.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div'
                mensagem_element = driver.find_element(By.CSS_SELECTOR, input_element)
            except:
                sleep(2)
                print("ERRO AO LOCALIZAR INPUT DE MENSAGEM")
                logging.critical("ERRO AO LOCALIZAR INPUT DE MENSAGEM")
                self.nao_enviados.append(p)
                pass
        try:
            mensagem_element.click()
        except:
            try:
                driver.execute_script('arguments[0].click();', mensagem_element)
            except:
                print("ERRO AO CLICAR NO ELEMENTO DE MENSAGEM")
                logging.critical("ERRO AO CLICAR NO ELEMENTO DE MENSAGEM")
                pass

        print("INPUT SELECIONADO")
        logging.info("INPUT SELECIONADO")
        sleep(0.5)
        try:
            mensagem_element.clear()
            mensagem_element.send_keys(self.mensagem)
            mensagem_element.send_keys(Keys.RETURN)
        except:
            print("ESTE PERFIL NÃO PERMITE ENVIO DE MENSAGENS")
            logging.info("ESTE PERFIL NÃO PERMITE ENVIO DE MENSAGENS")
            self.nao_enviados.append(p)
            try:
                index_element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div[4]/a")
                index_element.send_keys(Keys.RETURN)
            except:
                try:
                    index_element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/a/h2")
                    index_element.send_keys(Keys.RETURN)
                except:
                    print("ERRO AO ACIONAR PERFIL.")
                    logging.critical("ERRO AO ACIONAR PERFIL.")
                    pass
        self.enviados.append(p)
        print(f"MENSAGEM ENVIADA COM SUCESSO PARA {p}")
        logging.info(f"MENSAGEM ENVIADA COM SUCESSO PARA {p}")
        sleep(0.5)   
    def RetiraSalvo(self, p):
        driver = self.driver
        save_icon = 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div._ae65 > div > div > div._ae2s._ae3v._ae3w > section._aamu._ae3_._ae47._ae48 > span._aamz > div'
        try:
            save_element = driver.find_element(By.CSS_SELECTOR, save_icon)
        except:
            try:
                save_icon = '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div'
                save_element = driver.find_element(By.CSS_SELECTOR, save_icon)
            except:
                print("ELEMENTO NÃO encontrado")
                logging.critical("ELEMENTO NÃO encontrado")
                pass
        save_element.click()
        print(F"PUBLICAÇÃO DE {p} RETIRADA DA LISTAGEM DE SALVOS")
        logging.info(F"PUBLICAÇÃO DE {p} RETIRADA DA LISTAGEM DE SALVOS")
        sleep(0.5)
    def AcessaPerfis(self):
        driver = self.driver
        profile_list = self.profile_list
        print("INICIANDO ACESSO AOS PERFIS")
        print(profile_list)
        logging.info("INICIANDO ACESSO AOS PERFIS")
        logging.info(profile_list)
        item = 1
        for p in profile_list:
            try:
                driver.get(f"https://www.instagram.com/{p}/")
                sleep(2)
                mensagem_btn = "#mount_0_0_oF > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > header > section > div.x6s0dn4.x78zum5.x1q0g3np.xs83m0k.xeuugli.x1n2onr6 > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xmn8rco.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1i64zmx.x1n2onr6.x6ikm8r.x10wlt62.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div"
                try:
                    mensagem_element = driver.find_element(By.CSS_SELECTOR, mensagem_btn)
                    print("BUSCANDO ELEMENTO POR CSS...")
                    logging.info("BUSCANDO ELEMENTO POR CSS...")
                except NoSuchElementException:
                    try:
                        print("BUSCANDO ELEMENTO POR HTML...")
                        logging.info("BUSCANDO ELEMENTO POR HTML...")
                        mensagem_btn = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div"
                        mensagem_element = driver.find_element(By.XPATH, mensagem_btn)
                    except NoSuchElementException:
                        try:
                            print("BUSCANDO ELEMENTO POR CSS TENTATIVA 2...")
                            logging.info("BUSCANDO ELEMENTO POR CSS TENTATIVA 2...")
                            mensagem_btn = "#mount_0_0_Us > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > header > section > div.x6s0dn4.x78zum5.x1q0g3np.xs83m0k.xeuugli.x1n2onr6 > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xmn8rco.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1i64zmx.x1n2onr6.x6ikm8r.x10wlt62.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div"
                            mensagem_element = driver.find_element(By.CSS_SELECTOR, mensagem_btn)
                        except:
                            try:
                                print("BUSCANDO ELEMENTO POR HTML TENTATIVA 2...")
                                logging.info("BUSCANDO ELEMENTO POR HTML TENTATIVA 2...")
                                mensagem_btn = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div"
                                mensagem_element = driver.find_element(By.XPATH, mensagem_btn)
                            except:
                                print("ELEMENTO NÃO LOCALIZADO")
                                print(f"MENSAGEM PARA {p} NÃO ENVIADA")
                                logging.critical("ELEMENTO NÃO LOCALIZADO")
                                logging.critical(f"MENSAGEM PARA {p} NÃO ENVIADA")
                                self.nao_enviados.append(p)
                                continue        
                mensagem_element.click()
                print("BOTÃO MENSAGEM CLICADO")
                logging.info("BOTÃO MENSAGEM CLICADO")
                sleep(3)
            except:
                logging.critical(f"ERRO AO ACESSAR PERFIL {p}")
                return print(f"ERRO AO ACESSAR PERFIL {p}")
            print(f"PERFIL {p} ACESSADO COM SUCESSO!")
            logging.info(f"PERFIL {p} ACESSADO COM SUCESSO!")
            if(item == 1):
                self.FecharNotificacao()
            self.EnviaMsg(p)
            item += 1
        self.ApresentaLog()
    def ApresentaLog(self):
        print("PROCEDIMENTO FINALIZADO!")
        logging.info("PROCEDIMENTO FINALIZADO!")
        enviados = self.enviados
        total = self.profile_list
        nao_enviados = self.nao_enviados
        if(len(total) == 0):
            print("NÃO EXISTEM PUBLICAÇÕES NA LISTAGEM DE SALVOS")
            logging.info("NÃO EXISTEM PUBLICAÇÕES NA LISTAGEM DE SALVOS")
        else:
            print(f"{len(enviados)} Mensagens enviadas de {len(total)} perfils salvos \n")
            print("PERFIS ACIONADOS COM SUCESSO:")
            logging.info(f"{len(enviados)} Mensagens enviadas de {len(total)} perfils salvos \n")
            logging.info("PERFIS ACIONADOS COM SUCESSO:")
            for item in enviados:
                print(item)
                logging.info(item)
            if(len(nao_enviados) > 0):
                print("\nPERFIS NÃO ACIONADOS:")
                logging.info("\nPERFIS NÃO ACIONADOS:")
                for iten in nao_enviados:
                    print(iten)
                    logging.info(iten)
            else:
                print("TODOS OS PERFIS FORAM ACIONADOS COM SUCESSO")
                logging.info("TODOS OS PERFIS FORAM ACIONADOS COM SUCESSO")
        return print("PROCESSO FINALIZADO \n\n")
    def AdicionaPerfil(self, profile):
        profile_list = self.profile_list
        if profile in profile_list:
            print("PERFIL JÁ INCLUIDO")
            logging.warning("PERFIL JÁ INCLUIDO")
        else:
            profile_list.append(profile)
# mzx_docod    semprejv
# 'jv_moreiiraa', 'Semprejv@@11'
