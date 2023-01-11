import datetime
from spy import logging
from data_manager import GetSheetData, AddToSheetData, DelFromSheetData
from data_provider import WriteSheetData
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def help_command(update: Update, context: ContextTypes):
    result_msg = f'/help\n/get\n/getall\n/add\n/del'
    await update.message.reply_text(result_msg)
    logging(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), update.effective_user.first_name + str(update.effective_user.id), update.message.text, result_msg)

async def start_command(update: Update, context: ContextTypes):
    result_msg = f'/hello\n/time\n/sum - sum of numbers like "/sum 6 8" result "14"\n/help'
    await update.message.reply_text(result_msg)
    logging(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), update.effective_user.first_name + str(update.effective_user.id), update.message.text, result_msg)
    WriteSheetData(update.effective_user.id, "")

async def get_command(update: Update, context: ContextTypes):
    result_msg = f'{GetSheetData(update.effective_user.id, datetime.datetime.now())}'
    await update.message.reply_text(result_msg)
    logging(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), update.effective_user.first_name + str(update.effective_user.id), update.message.text, result_msg)

async def getall_command(update: Update, context: ContextTypes):
    result_msg = f'{GetSheetData(update.effective_user.id)}'
    await update.message.reply_text(result_msg)
    logging(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), update.effective_user.first_name + str(update.effective_user.id), update.message.text, result_msg)

async def add_command(update: Update, context: ContextTypes):
    AddToSheetData(update.message.text, update.effective_user.id)
    result_msg = f'Added'
    await update.message.reply_text(result_msg)
    logging(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), update.effective_user.first_name + str(update.effective_user.id), update.message.text, result_msg)

async def del_command(update: Update, context: ContextTypes):
    DelFromSheetData(update.message.text, update.effective_user.id)
    result_msg = f'Deleted'
    await update.message.reply_text(result_msg)
    logging(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), update.effective_user.first_name + str(update.effective_user.id), update.message.text, result_msg)
