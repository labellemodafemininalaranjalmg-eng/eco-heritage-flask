from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'desenvolvimento-eco-heritage-2026'  # Necessário para usar session

# Simulação de banco de dados de produtos
products = {
    1: {
        'nome': 'Blazer Cânhamo Heritage',
        'preco': 'R$ 890,00',
        'imagem': 'blazer_heritage.png',
        'descricao': 'Alfaiataria clássica em fibra de cânhamo orgânico.',
        'origem': 'Tecelagem Sustentável MG',
        'material': '100% Cânhamo Orgânico',
        'artesao': 'Oficina de Alfaiataria Solidária'
    },
    2: {
        'nome': 'Calça Pantalona Terra',
        'preco': 'R$ 560,00',
        'imagem': 'pantalona_terra.png',
        'descricao': 'Corte fluido com tingimento natural de casca de barbatimão.',
        'origem': 'Cooperativa de Algodão PB',
        'material': 'Algodão Orgânico Certificado',
        'artesao': 'Grupo Renda do Amanhã'
    }
}

@app.route('/')
def index():
    # Precisamos passar o dicionário de produtos para o template
    return render_template('index.html', produtos=products)

@app.route('/produto/<int:product_id>')
def product_detail(product_id):
    product = products.get(product_id)
    return render_template('product.html', product=product)

@app.route('/adicionar/<int:id>')
def adicionar_ao_carrinho(id):
    if 'carrinho' not in session:
        session['carrinho'] = []
    
    # Adiciona o ID do produto à lista do carrinho
    session['carrinho'].append(id)
    session.modified = True
    return redirect(url_for('exibir_carrinho'))

@app.route('/carrinho')
def exibir_carrinho():
    itens = []
    total = 0
    if 'carrinho' in session:
        for id_prod in session['carrinho']:
            p = products.get(id_prod)  # Usa o ID do produto para acessar o dicionário
            if p:
                itens.append(p)
    return render_template('cart.html', itens=itens)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Aqui você processaria os dados do formulário
        session.pop('carrinho', None) # Limpa o carrinho após a "compra"
        return render_template('sucesso.html')
    return render_template('checkout.html')


if __name__ == '__main__':
    app.run(debug=True)