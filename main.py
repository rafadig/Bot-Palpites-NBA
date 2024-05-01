from bs4 import BeautifulSoup
import requests

url = "https://www.sportytrader.com/pt-br/palpites/basquete/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    matches = soup.find_all("div", class_="border border-solid border-gray-300 h-card-prono p-4 rounded-md relative cursor-pointer hover:border-primary-yellow")
    
    for match in matches:
        schedule = match.find("p", class_="text-center text-xs mt-2 dark:text-white").text.strip()

        event = match.find("span", class_="text-balance tex-center block px-10").text.strip()

        team_names = match.find_all("span", class_="font-semibold text-center flex min-h-[45px] dark:text-white")
        team1_name = team_names[0].text.strip()
        team2_name = team_names[1].text.strip()

        prediction = match.find("p", class_="text-center font-semibold").text.strip()

        print("⌚️", schedule)
        print("🏀", event)
        print("⛹️ ", team1_name)  # Adicionando um espaço após o emoji
        print("⛹️‍♂️", team2_name)
        print("🟢", prediction)
        print()
else:
    print("Falha ao acessar a página. Código de status:", response.status_code)
