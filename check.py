import requests
import time

start = time.time()

print('Downloading domain list')

url = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"
r = requests.get(url)

with open("domain_list.txt", 'wb') as f:
	f.write(r.content)


file = open("domain_list.txt")
domains = file.readlines()

sld = input("Enter website name: ")

for domain in domains[1:]:
	while True:
		try:
			url = "http://" + sld + "." + domain.strip()
			x = requests.get(url)
			if x.status_code == 200:
				print(url)
			break
		except KeyboardInterrupt:
			print('Last tested URL', url)
			print(time.time() - start)
			exit()
		except:
			break

print(time.time() - start)