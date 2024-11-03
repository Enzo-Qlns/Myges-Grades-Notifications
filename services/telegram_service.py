import requests


class TelegramService:
    def __init__(self, token: str, channel_id: str, logger):
        self.token = token
        self.channel_id = channel_id
        self.api_url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        self.logger = logger

    def send_message(self, message: str):
        """
        Envoie un message sur le canal Telegram
        :param message: String
        :return:
        """
        data = {
            "chat_id": self.channel_id,
            "text": message,
        }

        response = requests.post(self.api_url, data=data)
        if response.status_code == 200:
            self.logger.info("Message envoyé avec succès.")
            print("Message envoyé avec succès.")
        else:
            self.logger.error(f"Erreur lors de l'envoi du message : {response.status_code} - {response.text}")
            print(f"Erreur lors de l'envoi du message : {response.status_code} - {response.text}")