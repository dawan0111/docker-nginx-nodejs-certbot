import os

if __name__ == "__main__":
  print("ssl installer")
  email = input("Enter your email: ")
  domains = []
  while True:
    domain = input("Enter your domain:")
    if domain == "":
      break
    domains.append("-d {0}".format(domain))

  try:
    os.system("""
      docker run -it --rm --name certbot \
      -v './certbot/etc:/etc/letsencrypt/:rw' \
      -v './certbot/var:/var/lib/letsencrypt/:rw' \
      -v './certbot/www:/var/www/certbot/:rw' \
      certbot/certbot \
      certonly --webroot --webroot-path=/var/www/certbot --email {0} --agree-tos --no-eff-email --force-renewal {1}
    """.format(email, " ".join(domains)))
  except Exception as e:
    print(e)
  