from CNN import get_CNN
from keras.callbacks import EarlyStopping
#from LSTM import get_LSTM
from Load_Data import load_train, load_test, shuffle_data
from keras import utils

col = ['Current 1', 'Current 2', 'Current 3', 'Voltage 1', 'Voltage 2', 'Voltage 3', 'Accelerometer 1', 'Accelerometer 2', 'Microphone', 'Tachometer', 'Temperature', 'Output Current', 'Output Voltage']
train, label = load_train(col, '/media/meng/9079-7B0D/clean_data/train/', 6)
test, test_y = load_test(col, "/media/meng/9079-7B0D/clean_data/test/")

train, label = shuffle_data(train, label)

train = train.reshape(train.shape[0], 200, 13, 1)
test = test.reshape(test.shape[0], 200, 13, 1)

#train = train.reshape(train.shape[0], 1, 200, 13, 1)
#test = test.reshape(test.shape[0], 1, 200, 13, 1)

types = 28

label = utils.to_categorical(label, num_classes=types)
test_y = utils.to_categorical(test_y, num_classes=types)
model = get_CNN()
early_stopping = EarlyStopping(monitor='val_loss', patience=2)
model.fit(train, label, batch_size=240, nb_epoch=100, callbacks=[early_stopping], verbose=1, shuffle=True, validation_data=(test, test_y))
json_string = model.to_json()
#open('model.json','w').write(json_string) 
#model.save_weights('model.h5')
