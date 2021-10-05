#PART 2
#2 Open the CupcakeInvoices.csv.
open_file = open('CupcakeInvoices.csv')

#3 Loop through all the data and print each row.
for line in open_file:
  print(line)

#4 Loop through all the data and print the type of cupcakes purchased.
for line in open_file:
  value = line.split(',')
  print(value[2])

#5 Loop through all the data and print out the total for each invoice
#(Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
for line in open_file:
  value = line.split(',')
  quality = int(value[3])
  price = float(value[4])
  total = (quality * price)
  print(total)

#6 Loop through all the data, and print out the total for all invoices combined.
total_invoice = 0
for line in open_file:
  value = line.split(',')
  quality = int(value[3])
  price = float(value[4])
  total = (quality * price)
  total_invoice = total + total_invoice

print(total_invoice)


#7
open_file.close()
