from mailjet_rest import Client
from config import settings
from exceptions import ErrorResponse


class MailService:
    def __init__(self, logger) -> None:
        self.MAILJET_API_KEY = settings.MAILJET_API_KEY
        self.MAILJET_SECRET_KEY = settings.MAILJET_SECRET_KEY
        self.MAILJET_SENDER_EMAIL = settings.MAILJET_SENDER_EMAIL
        self.DESTINATION_EMAIL = settings.DESTINATION_EMAIL
        self.logger = logger

    def send_message(self, message: str) -> None:
        try:
            api_key = self.MAILJET_API_KEY
            api_secret = self.MAILJET_SECRET_KEY
            mailjet = Client(auth=(api_key, api_secret), version='v3.1')
            data = {
                'Messages': [
                    {
                        "From": {
                            "Email": self.MAILJET_SENDER_EMAIL,
                        },
                        "To": [
                            {
                                "Email": self.DESTINATION_EMAIL,
                            }
                        ],
                        "Subject": "Nouvelle note",
                        "TextPart": "Salut ! Tu as une nouvelle note !",
                        "HTMLPart": message
                    }
                ]
            }
            result = mailjet.send.create(data=data)
            if result.status_code != 200:
                raise ErrorResponse(f"Erreur lors de l'envoi du message : {result.json()}")

            self.logger.info("Erreur lors de l'envoi du message : %s", result.json())
            print("E-mail envoyé avec succès !")

        except Exception as e:
            raise ErrorResponse(f"Erreur lors de l'envoi du message : {str(e)}")

    @staticmethod
    def template_message_grades(grades: str) -> str:
        message = f"""
            <html>
                <head>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            background-color: #e3f2fd; /* Bleu ciel doux */
                            color: #333;
                            margin: 0;
                            padding: 20px;
                        }}
            
                        p {{
                            line-height: 1.6;
                            font-size: 16px;
                        }}
            
                        .header {{
                            background-color: #42a5f5; /* Bleu plus soutenu */
                            color: white;
                            padding: 10px;
                            text-align: center;
                            font-size: 24px;
                            font-weight: bold;
                            border-radius: 8px;
                        }}
            
                        .content {{
                            background-color: white;
                            padding: 20px;
                            border-radius: 8px;
                            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                            margin-top: 20px;
                        }}
            
                        .grades {{
                            font-weight: bold;
                            color: #42a5f5; /* Bleu ciel pour les notes */
                        }}
                    </style>
                </head>
                <body>
                    <div class="header">
                        Nouvelle note !
                    </div>
                    <div class="content">
                        <p>Voici les nouvelles notes : <span class="grades">{grades if type(grades) == str else ", ".join(grades)}</span></p>
                    </div>
                </body>
            </html>
        """
        return message

    @staticmethod
    def template_message_exam(grades: str) -> str:
        message = f"""
            <html>
                <head>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            background-color: #e3f2fd; /* Bleu ciel doux */
                            color: #333;
                            margin: 0;
                            padding: 20px;
                        }}

                        p {{
                            line-height: 1.6;
                            font-size: 16px;
                        }}

                        .header {{
                            background-color: #42a5f5; /* Bleu plus soutenu */
                            color: white;
                            padding: 10px;
                            text-align: center;
                            font-size: 24px;
                            font-weight: bold;
                            border-radius: 8px;
                        }}

                        .content {{
                            background-color: white;
                            padding: 20px;
                            border-radius: 8px;
                            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                            margin-top: 20px;
                        }}

                        .grades {{
                            font-weight: bold;
                            color: #42a5f5; /* Bleu ciel pour les notes */
                        }}
                    </style>
                </head>
                <body>
                    <div class="header">
                        Nouvelle note !
                    </div>
                    <div class="content">
                        <p>Voici les nouvelles notes : <span class="grades">{grades}</span></p>
                    </div>
                </body>
            </html>
        """
        return message
