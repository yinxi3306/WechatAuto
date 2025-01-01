import itchat
keywords = {


    'hello': 'Hello! How can I help you?',


    'weather': 'Today is sunny!',


    'bye': 'Goodbye!'


}
@itchat.msg_register(itchat.content.TEXT)


def text_reply(msg):


    text = msg['Text'].lower()


    for keyword in keywords:


        if keyword in text:


            return keywords[keyword]


    return 'Sorry, I did not understand that.'


itchat.auto_login()


itchat.run()