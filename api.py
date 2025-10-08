import requests

url = "https://api.languagetool.org/v2/check"
data = {
    "text": "He go to school every day.",
    "language": "en-US"
}

response = requests.post(url, data=data)
result = response.json()

# Print errors and suggestions in a clear format
if "matches" in result:
    for match in result["matches"]:
        print("🚨 Error:", match["message"])
        print("🔴 Text:", match["context"]["text"])
        print("➡️  Error position:", match["offset"], "-", match["offset"] + match["length"])
        if match.get("replacements"):
            suggestions = [rep["value"] for rep in match["replacements"]]
            print("✅ Suggestions:", ", ".join(suggestions))
        print("-" * 50)
else:
    print("✔️ No errors found")
