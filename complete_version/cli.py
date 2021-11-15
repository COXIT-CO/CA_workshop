from complete_version.external_systems.miro_interface import MiroApiClient

AUTH_TOKEN = '7avPu0XGaswfMPGRTQ1ufVWtVrs'
BOARD_ID = 'o9J_ljuLrH8='
DB_PATH = 'ids.json'

if __name__ == "__main__":
    print("Welcome to the practical part of the workshop!")
    choice = -1
    client = MiroApiClient(base_url='https://api.miro.com',
                           auth_token=AUTH_TOKEN)

    while choice < 1 or choice > 5:
        if choice != -1:
            print("Don't try to cheat. Possible answers: 1, 2, 3, 4, 5")
        choice = int(input("Enter your choice:  "))

    result = client.vote_for_code_with_number(BOARD_ID, choice)

    if result.status_code == 200:
        print("Great! Thanks for your answer")
