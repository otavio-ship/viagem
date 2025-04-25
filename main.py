from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calcular_tempo_viagem():
    if request.method == 'POST':
        try:
            distancia = float(request.form['distancia'])
            velocidade = float(request.form['velocidade'])

            if distancia <= 0:
                return render_template('tempo.html', erro="A distância deve ser maior que zero!")
            if velocidade <= 0:
                return render_template('tempo.html', erro="A velocidade deve ser maior que zero!")

            tempo = distancia / velocidade
            horas = int(tempo)
            minutos = int((tempo - horas) * 60)

            return render_template('tempo.html',
                                   distancia=distancia,
                                   velocidade=velocidade,
                                   horas=horas,
                                   minutos=minutos)

        except ValueError:
            return render_template('tempo.html', erro="Por favor, digite valores numéricos válidos!")

    return render_template('tempo.html')


if __name__ == '__main__':
    app.run(debug=True)