import smtplib
import random
import pickle
from collections import namedtuple

# Sprint - @pm.sprint.com
# ATAT - @txt.att.net


def send_txt(message_info):
    """
    Funtion to send email/text using gmail account
    :param message_info: a named tuple that should have an email, pass, phone number,
                        and the text body

    """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    # Login into email account - account and then password
    server.login(message_info.email, message_info.password)
    # Message body - my email, phone number, and message body
    server.sendmail(message_info.email, message_info.phone_number, message_info.text)
    server.quit()
    return


def get_lovin():
    """
    This was my original function to pull out a pickup line from my list.
    :return: txt_quote: String.  Its the pickup line
    """
    # Opens the text file with the lines, reads them into memory, and then closes the file
    love = open('/Users/lehassell/PycharmProjects/texting_fun/cleaned_text.txt', 'r')
    love_quotes = love.read()
    love.close()
    # Parses them out splits the string by line into a list (one pickup line per line)
    love_quotes = love_quotes.split('\n')
    # Gets a random line
    txt_quote = random.choice(love_quotes)
    return txt_quote


def smooth_lines():
    """
    The new "improved?" function to automatically generate pickup lines.
    :return:
        pickup_line: String, my generated line
    """
    # To do.  This was defined elsewhere.
    chain = pickle.load(open("/Users/lehassell/PycharmProjects/test_scrape/markov_practice/chain.p", "rb"))
    new_line = []
    sword1 = "BEGIN"
    sword2 = "NOW"

    while True:
        sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
        if sword2 == "END":
            break
        new_line.append(sword2)
    pickup_line = ' '.join(new_line)
    # I have to re-encode the text to send it out
    pickup_line = pickup_line.encode('utf-8')
    return pickup_line

# Start by getting out the login information from a local text
safety = open('/Users/lehassell/PycharmProjects/texting_fun/safety.txt', 'r')
use_pass = safety.read()
use_pass = use_pass.split(',')

# Markov chain the perfect pick-up line
txt_message = smooth_lines()
#print(txt_message)

# Build a named tuple to help keep track of info better
message = namedtuple('Person', 'email password phone_number text')

# Define tuples for use
GF = message(use_pass[0], use_pass[1], use_pass[3], txt_message)
Me = message(use_pass[0], use_pass[1], use_pass[5], txt_message)

# Send the text
send_txt(Me)
#send_txt(GF)



