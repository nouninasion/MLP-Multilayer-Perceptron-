import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = np.random.rand(100, 16)
y_class = np.random.randint(0, 4, size=100)

X_train, X_test, y_train, y_test = train_test_split(X, y_class, test_size=0.2, random_state=42)

mlp = MLPClassifier(hidden_layer_sizes=(8,), activation='relu', max_iter=1000, random_state=1)

mlp.fit(X_train, y_train)

y_pred = mlp.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("Akurasi:", acc)
print("Prediksi kelas (0=Kelas1, 3=Kelas4):", y_pred)
