import google.generativeai as genai

sec_key = userdata.get('gem-api')
genai.configure(api_key=sec_key)

model = genai.GenerativeModel("gemini-1.5-flash")
sample_pdf = genai.upload_file('2402.07927v1.pdf')

def summrize(sample_pdf):
  response = model.generate_content([
    "Sumarize este pdf, responda em 
    português-brasil", sample_pdf])
    
  return response

  
