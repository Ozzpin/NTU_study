{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fe62e795",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, render_template"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5862a8cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a593975e",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cdb15b91",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\", methods=[\"GET\", \"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        rates = float(request.form.get(\"rates\"))\n",
    "        model_1 = joblib.load(\"regression\")\n",
    "        r_1 = model_1.predict([[rates]])\n",
    "        model_2 = joblib.load(\"tree\")\n",
    "        r_2 = model_1.predict([[rates]])\n",
    "        return render_template(\"index.html\", result1 = r_1, result2 = r_2)\n",
    "    else:\n",
    "        return render_template(\"index.html\", result1 = \"WAITING\", result2 = \"WAITING\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ed3d0481",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [24/Jul/2022 20:29:31] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [24/Jul/2022 20:29:41] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50a5069f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
