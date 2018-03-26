from flask import Flask, redirect, url_for, request
import csv

app = Flask(__name__)

l=[]
time = ''
index = 0
@app.route('/<y>/<m>/<d>')
def main(y,m,d):
	index = -1
	with open('storm.csv', 'r', newline='') as f:
		for line in f:
			l.append(line.strip().split(','))
		time = y+m+d
		for i in range(len(l)):
			l[i][0] = l[i][0][3:10]
			l[i][0] = l[i][0].replace('*','')
			del(l[i][1])
			if l[i][0]==time:
				index = i
		with open('data.csv', 'w', newline='') as f1:
			writer = csv.writer(f1)
			writer.writerow(['year','population'])
			for j in range(1,27):
				writer.writerow([j]+[l[index][j]])
	return redirect('http://localhost:8080/index.html')
if __name__ == '__main__':
	app.run()