from src.extractor import extract_job_posting

# raw = """
# Senior ML Engineer at Acme Corp
# Location: Amsterdam, Netherlands (Hybrid)
# Salary: €80,000 - €110,000

# We are looking for a Senior ML Engineer to join our team.

# Requirements:
# - 5+ years of Python experience
# - Experience with LLMs and NLP
# - Strong understanding of ML fundamentals

# Skills needed: PyTorch, HuggingFace, Docker, AWS

# Benefits: 25 days holiday, pension, equipment budget, flexible hours
# """

raw = """
Machine Learning Engineer
At bunq, we're not just building a banking app; we're reshaping how people around the world experience financial freedom. As our Machine Learning Engineer, your mission is to build the intelligent shield that protects our users from fraud. You'll develop powerful, efficient ML systems that detect threats in real-time without ever getting in the way of a seamless banking experience.
Up for this?
Kick off your application by taking our assessment and find out if bunq is your perfect match! 🚀
Take Ownership
As our Machine Learning Engineer, you will build the foundational tools and govern the live models that keep our users safe. You'll:
Develop and own a generalized ML training framework that empowers our teams to build, train, and deploy fraud detection models with speed and consistency. 
Govern the end-to-end lifecycle of our supervised transaction monitoring models, ensuring they perform at their peak to protect our users' money in real-time. 
Partner closely with product and compliance teams to translate business needs into powerful ML solutions, continuously improving our models to stay ahead of emerging threats.
You have hands-on experience developing, training, and deploying machine learning models in a production cloud environment. 
You can apply and optimize a range of supervised and unsupervised machine learning models to solve real-world business problems. 
You excel at working with stakeholders like product and process owners, translating complex business requirements into technical ML solutions. 
You are highly proficient in Python and its common machine learning frameworks (bonus points for experience in object-oriented programming in PHP).
You are fluent in English - able to communicate effectively in a global team, ensuring collaboration and clarity across all project stages.
All new hires are subject to Pre-employment Screening (PES), which includes checks conducted by our third-party partner, DISA. This is part of our commitment to a secure and trustworthy workplace
Curious to see how we make life easy? - try the bunq app, it only takes 5 minutes to sign up.
Your space to perform
We give you the space and the tools you need to succeed 💪🏼
🤟 Great, international colleagues who share your mindset
👩‍💻 Hybrid setup: after 3 months in-office, work 2 days remote, 3 days in-office weekly.
🧳 Digital Nomad Program: After your first year, enjoy up to 20 days per year to work while traveling, combining flexibility with strong team collaboration
🚀 We reward tenure with a dedicated travel budget: €1.5k after 2 years and €3k after 4 years to visit another core office.
📚 We support growth with bunq Academy and €1500 annual learning budget
🚴 Massive discount with Urban Sports Club 💪
🚌 Travel expenses are covered whether you come walking or by bike, bus or car (though we prefer green choices 🌳)
💻 A MacBook so you can Get Shit Done with us
🥦 Delicious lunches from our fabulous in-house chefs with vegan and vegetarian options
💰 An optional pension plan with monthly contribution from bunq
💸 Monthly contribution to your phone and internet bills
🍻 Friday drinks and other celebrations - bunq style 
"""

job = extract_job_posting(raw)
print(job.model_dump_json(indent=2))
