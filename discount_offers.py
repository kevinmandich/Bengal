## discount_offers.py
## Challenge # 48

import os

import sys, string

with open(os.getcwd()+'\\discount_offers_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

punc = string.punctuation + ' 0123456789'

def strip_special_characters(text):
    text = text.lower()
    newText = ''
    for char in text:
        if ord(char) > 96 and ord(char) < 123:
            newText += char
    print newText

def weight(name, product):
    """Calculate the weight for an individual edge between a name and product.
    Rules
      1. Product with an even # of letters : Number of vowels in name * 1.5
      2. Product with odd # of letters : Number of consonants in name
      3. For each common factor > 1 for the number of letters in name & product
         multiply the score * 1.5
    """
    weight = 0.0
    num_product_letters = num_letters(product.lower())
    num_name_letters = num_letters(name.lower())

    if num_product_letters % 2 == 0:
        weight = num_vowels(name.lower()) * 1.5
    else:
        weight = num_consonants(name.lower())

    if euclid_gcd(num_product_letters, num_name_letters) > 1:
        weight = weight * 1.5

    return weight

def euclid_gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def count_chars(val, chars):
    count = 0
    for c in val:
        if c in chars:
            count += 1
    return count

def num_letters(val):
    return count_chars(val, 'abcdefghijklmnopqrstuvwxyz')

def num_vowels(val):
    return count_chars(val, 'aeiouy')

def num_consonants(val):
    return count_chars(val, 'bcdfghjklmnpqrstvwxz')

#names, products = [semi.split(',') for semi in line.strip().split(';')]
        
for case in testCases:
    #users, products = case.split(';')
    #users = [user.replace(' ','') for user in users.split(',')]
    #products = [strip_special_characters(product) for product in products.split(',')]
    names, products = [semi.split(',') for semi in case.strip().split(';')]
    for name in names:
        for product in products:
            print weight(name, product)
        print ''
    #print users,'\n'
    #print products, '\n\n'

















