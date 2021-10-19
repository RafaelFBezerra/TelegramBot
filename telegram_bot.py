import pieces

# Função responsável por criar o teclado de opções referente a tomada de decisão do BOT
def inicio(update: pieces.Update, context: pieces.CallbackContext):

    # Cria o teclado com seus respectivos rótulos e retornos para realizar rotinas distintas
    teclado = [
        [pieces.InlineKeyboardButton ("Verificar Status" , callback_data = 'Verificar Status')],
        [pieces.InlineKeyboardButton ( "Inicializar Execução" , callback_data = 'Inicializar Execução')],
        [pieces.InlineKeyboardButton ("Interromper Execução" , callback_data = 'Interromper Execução')]
        
    ]

    # Indica o Markup referente ao teclado
    reply_markup = pieces.InlineKeyboardMarkup(teclado)

    # Atribui o Markup do teclado a ele
    update.message.reply_text("Por favor, selecione uma das opções abaixo referente a aplicação:", reply_markup=reply_markup)

# Função responsável por armazenar o retorno da opção selecionada e realizar as tomadas de decisão
def botoes(update: pieces.Update, context: pieces.CallbackContext):

    # Atribui a variável o update da opção selecionada
    query = update.callback_query

    # Obtém a resposta do update capturado
    query.answer()

    # Obtém o callback_data referente a opção selecionada
    opcao_selecionada = query.data

    # Caso a opção selecionada seja "Verificar Status", deve retornar se a aplicação está em execução ou se está inativa
    if opcao_selecionada == "Verificar Status":
        query.edit_message_text("A aplicação encontra-se em... ")

    # Caso a opção selecionada seja "Inicializar Execução", deve inicializar a aplicação
    elif opcao_selecionada == "Inicializar Execução":

        # Retorna a opção selecionada
        query.edit_message_text("Inicializando execução...")

    # Por fim, caso a opção selecionada seja "Interromper Execução", deve interromper a aplicação
    else:

        # Retorna a opção selecionada
        query.edit_message_text("Interrompendo execução...")

# Função responsável por orientar o usuário ao digitar o comando /ajuda
def comando_ajuda (update: pieces.Update, context: pieces.CallbackContext):
    update.message.reply_text("Por favor, envie ou clique em /iniciar para inicializar o Bot")

# Função responsável por inicializar o BOT do Telegram
def bot_telegram_main():
    
    # Cria rotina responsável por capturar as solicitações invocadas ao BOT
    updater = pieces.Updater(token=pieces.global_vars.token_bot_telegram, use_context=True)

    # Adiciona os Handles referente as funcionalidades do BOT
    updater.dispatcher.add_handler(pieces.CommandHandler("iniciar", inicio))
    updater.dispatcher.add_handler(pieces.CallbackQueryHandler(botoes))
    updater.dispatcher.add_handler(pieces.CommandHandler("ajuda", comando_ajuda))

    # Starta a instância do BOT
    updater.start_polling()
    updater.idle()
    
