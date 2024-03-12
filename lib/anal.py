import re
from dotenv import load_dotenv
import os
import datetime

def extract_values_from_html(html):
    pattern = r'<tr>\s*<td class="left">(.+?)</td>\s*<td class="left">(.+?)</td>\s*<td class="text-right">(.+?)</td>\s*<td class="text-right">\s*([\d\.,]+)\s*</td>\s*<td class="text-right">\s*([\d\.,]+)\s*</td>\s*<td class="text-right">\s*([\d\.,]+)\s*</td>\s*<td class="text-right">\s*([\d\.,]+)\s*</td>\s*<td class="text-right">\s*([\d\.,-]+)\s*</td>\s*<td class="text-right">\s*([\d\s]+)\s*</td>\s*<td class="text-right">\s*([\d\s]+)\s*</td>\s*<td class="text-right">\s*([\d\s,]+)\s*</td>\s*</tr>'
    
    matches = re.findall(pattern, html, re.DOTALL)
    
    values_list = []
    for match in matches:
        values_list.append(list(match))
    
    return values_list

def anal():
    try:
        tmp = open(os.getenv("FILENAME")).read()
        tab = extract_values_from_html(str(tmp))

        act_time = datetime.datetime.now()

        with open(f"out_data_{act_time.strftime('%Y-%m-%d_%H-%M-%S')}.txt", "w") as file:
            for i in tab:
                file.write(str(i) + "\n")

    except OSError as e:
        print("Error: ", e)