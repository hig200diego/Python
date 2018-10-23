import webbrowser

websites = ['g', 'f'] #lista com as iniciais dos sites

while True: # verifica se a inicial digitada existe e faz repetir a pergunta do input caso a letra não esteja na lista
    siteInput = (input('Insira a letra inicial do site que desejas navegar: '))
    if siteInput in websites:
         print('Página encontrada! Aguarde...')
         break
    else:
        print('Página não encontrada, tente novamente.')
     

if siteInput == websites[0]: #abre o site
    webbrowser.open('https://www.google.com.br/')
        
elif siteInput == websites[1]:
     webbrowser.open('https://pt-br.facebook.com/')
else:
     print('Tente outra vez')
