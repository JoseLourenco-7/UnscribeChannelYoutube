import re
from playwright.sync_api import sync_playwright
from time import sleep


with (sync_playwright() as p):
    nav = p.firefox.launch(headless=False)
    page = nav.new_page()
    page.goto("https://www.youtube.com/feed/channels")

    sleep(10)

email = "adicione aqui seu email"
    # encotra e preeche o campo de email
    page.locator('xpath=//*[@id="identifierId"]').click()
    page.fill('xpath=//*[@id="identifierId"]', email)
    page.locator('xpath=//*[@id="identifierNext"]/div/button/div[3]').click()
    sleep(20)

    # por segurança não adicione aqui sua senha, pode digitar manualmente no navegador.

    # Espere até que os elementos com a classe 'style-scope ytd-expanded-shelf-contents-renderer' sejam carregados
    page.wait_for_selector('.style-scope.ytd-expanded-shelf-contents-renderer')

    # Localize todos os elementos com a classe 'style-scope ytd-expanded-shelf-contents-renderer'
    elementos = page.query_selector_all('.style-scope.ytd-expanded-shelf-contents-renderer')

    # Itere pelos elementos
    for elemento in elementos:
        # Localize o botão com a classe 'yt-spec-touch-feedback-shape__fill' dentro do elemento
        Subscrito = elemento.query_selector('#notification-preference-button > ytd-subscription-notification-toggle-button-renderer-next > yt-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill')

        # Verifica se o botão "Subscrito" está visível antes de clicar nele
        if Subscrito and Subscrito.is_visible():
            Subscrito.click()
            print("Botão Subscrito está disponivel")
            sleep(1)

            anularSubs = page.query_selector('#items > ytd-menu-service-item-renderer:nth-child(4) > tp-yt-paper-item > yt-formatted-string')

            # Verifica se o elemento "Anular inscrição" está visível antes de clicar nele
            if anularSubs and anularSubs.is_visible():
                anularSubs.click()
                print("Anulação de inscrição realizada.")
                sleep(1)
                anularSubs2 = page.query_selector('#confirm-button > yt-button-shape > button > yt-touch-feedback-shape > div')

                if anularSubs2:
                    anularSubs2.click()
                    sleep(1)
                    print("Anular sub 2 realizado")
                else:
                    print("Não foi possivel clicar no elemento anular sub 2")
            else:
                print("Elemento 'Anular inscrição' não está visível.")
        else:
            print("Botão 'Subscrito' não encontrado ou não está visível na classe.")

    sleep(3000)
    page.close()