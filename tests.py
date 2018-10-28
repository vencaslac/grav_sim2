with open('stars.txt','rt') as f:
    stars = f.read().replace('\n\n','\n')
    stars=stars.replace('\n',',')
    stars=stars.replace(',,',',')
    stars=stars.replace(',',"',\\\n'")

print(stars)
