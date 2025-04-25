
from flask import Flask, request, render_template_string, redirect
import csv

app = Flask(__name__)

html_form = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Formulário de Arepas</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 30px; background: #fff8f0; }
    h2 { color: #d2691e; }
    form { background: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
    p { font-weight: bold; }
    input[type="text"] { width: 90%; padding: 8px; margin-bottom: 10px; }
    input[type="submit"] { padding: 10px 20px; background: #ffa500; border: none; color: white; cursor: pointer; border-radius: 5px; }
    input[type="submit"]:hover { background: #ff8c00; }
    img { width: 120px; margin: 10px 0; border-radius: 8px; }
  </style>
</head>
<body>
  <h2>Formulário de Arepas</h2>
  <form method="POST">
    <p>Qual Arepa você escolheria para comer?</p>
    <img src="https://via.placeholder.com/120?text=Arepa" alt="Arepa"><br>
    <input type="text" name="arepa" required>

    <p>Se tivesse que escolher 6 sabores, quais desses escolheria? (separe por vírgula)</p>
    <img src="https://via.placeholder.com/120?text=Sabores" alt="Sabores"><br>
    <input type="text" name="sabores" required>

    <p>Que dia da semana seria o perfeito para você degustar uma arepa?</p>
    <img src="https://via.placeholder.com/120?text=Semana" alt="Semana"><br>
    <input type="text" name="dia" required>

    <br><br>
    <input type="submit" value="Enviar Respostas">
  </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        arepa = request.form['arepa']
        sabores = request.form['sabores']
        dia = request.form['dia']

        with open('respostas.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([arepa, sabores, dia])

        return render_template_string("""
        <h2 style='color:#d2691e;'>🎉 Obrigado pela participação!</h2>
        <p style='font-size:18px;'>Esperamos futuramente poder te oferecer a sua arepa escolhida! 🌽✨</p>
        <a href='/'>Voltar ao formulário</a>
        """)

    return render_template_string(html_form)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
