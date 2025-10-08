from flask import Flask, request, jsonify, send_from_directory
import language_tool_python
import os

app = Flask(__name__)

# تهيئة أداة التدقيق النحوي
tool = language_tool_python.LanguageTool('en-US')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/check-grammar', methods=['POST'])
def check_grammar():
    try:
        data = request.json
        text = data.get('text', '')
        
        # اكتشاف الأخطاء
        matches = tool.check(text)
        
        # تطبيق التصحيحات
        corrected_text = language_tool_python.correct(text, matches)
        
        # تحضير الاستجابة
        errors = []
        for match in matches:
            errors.append({
                'message': match.message,
                'offset': match.offset,
                'length': match.length,
                'replacements': match.replacements[:5],  # أول 5 اقتراحات فقط
                'ruleId': match.ruleId
            })
        
        return jsonify({
            'originalText': text,
            'correctedText': corrected_text,
            'errors': errors,
            'errorsCount': len(matches),
            'success': True
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
