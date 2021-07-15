import tensorflow as tf
import numpy as np

def train_mnist(filename):
    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    y_train = tf.keras.utils.to_categorical(y_train)
    y_test = tf.keras.utils.to_categorical(y_test)
    x_train = x_train.reshape(
        x_train.shape[0], x_train.shape[1], x_train.shape[2], 1
    )
    x_test = x_test.reshape(
        x_test.shape[0], x_test.shape[1], x_test.shape[2], 1
    )

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(
            32, (3, 3), activation="relu", input_shape=(28, 28, 1)
        ),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(10, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )
    model.fit(x_train, y_train, epochs=10)

    model.evaluate(x_test,  y_test, verbose=2)
    model.save(filename)

def classify(model, pixels):
    model = tf.keras.models.load_model(model)
    classification = model.predict(
        [np.array(pixels).reshape(1, 28, 28, 1)]
    )
    confidence = classification[0][classification.argmax()]
    classification = classification.argmax()
    return classification, confidence