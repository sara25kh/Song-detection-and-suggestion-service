import requests
def send_simple_message(recommendations):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox6e68c9624593447080c7e61163d0ab36.mailgun.org/messages",
		auth=("api", "c3d48abcc190ef2e65825e85753c0640-b02bcf9f-689db24a"),
		data={"from": "Mailgun Sandbox <postmaster@sandbox6e68c9624593447080c7e61163d0ab36.mailgun.org>",
			"to": ["sara <sarakhatir2001@gmail.com>", "sara <sara25_kh@aut.ac.ir>"],
			"subject": "recommendation songs",
			"text": recommendations})

# You can see a record of this email in your logs: https://app.mailgun.com/app/logs.

# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain so you can send 10000 emails/month for free.

# send_simple_message('recommendations')