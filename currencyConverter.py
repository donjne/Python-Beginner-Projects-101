def main():
    print('This program converts US dollars to Nigerian naira')
    print()

    dollars = eval(input('Enter the amount in dollars: '))

    naira = convert_to_naira(dollars)

    print('That is', naira, 'NGN')

convert_to_naira = lambda naira: naira * 980