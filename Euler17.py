# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 

print("started program")

# decimals:
ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds = ['', 'onehundredand', 'twohundredand', 'threehundredand', 'fourhundredand', 'fivehundredand', 'sixhundredand', 'sevenhundredand', 'eighthundredand', 'ninehundredand']

sum = 0
count = -1 # this accounts for the first thing being '' + '' + '', setting it to 0

for i in range(0, 10):
    for k in range(0, 10):
        sum += len(hundreds[i]) + len(teens[k]) # hundreds + and + teen
        count+=1
        print(hundreds[i] + teens[k])

    for j in range(0, 9):
        for k in range(0, 10):
            sum += len(hundreds[i]) + len(tens[j]) + len(ones[k])
            count+=1
            print(hundreds[i] + tens[j] + ones[k])

sum += len("onethousand")
# account for hundreds without an and, i.e. 100, 200, 300 etc.
sum -= 9 * 3

count += 1
print(sum)
print(count)