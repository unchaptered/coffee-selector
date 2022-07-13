@app.route('/nespresso', methods=['GET'])
def show_nespresso():
    name = request.form['name']
    return render_template('./pages/select.html', title='캡슐커피 취향저격',name=name)

@app.route("/nespresso", methods=["POST"])
def save_nespresso():
    cake_receive = request.form['cake_give']
    apple_receive = request.form['apple_give']
    strength_receive = request.form['strength_give']
    milk_receive = request.form['milk_give']
    size_receive = request.form['size_give']

    doc = {
        'cake': cake_receive,
        'apple': apple_receive,
        'strength': strength_receive,
        'milk': milk_receive,
        'size': size_receive
    }
    db.movies.insert_one(doc)

    return jsonify({'msg': '선택 완료!'})