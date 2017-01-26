# Deep learning course

I am participating in the deep learning MOOC from http://fast.ai. Usually late at night, and hence in small batches. I use the present markdown file for log-keeping and managing to-do lists, in order to be independent of the computer I am working on.

# Infrastructure and workflow

For training CNNs, I will use an AWS p2.large instance. Setting things up and running will be done on a much cheaper t2.large instance. To synchronize the machines, I will use the present github repository.

# Week 1

In week one, we are expected to set up an AWS p2.large instance and get keras on top of theano up and running. We use this instance to retrain a VGG 16 model to discriminate between cats and dogs. 

As a homework, we have to participate in the cats vs dogs redux challenge on http://kaggle.com, using a fine-tuned VGG16 model.

## To do

A general to-do list is managed here, finer details will be handled in a jupyter notebook.

- [x] get p2.large machine up and running
- [x] get competition data handling script up and running (inside a notebook?)
- [x] Train and finetune on p2.large instance!
- [ ] Visualize results: correctly classified, incorrectly classified and so on, in the notebook
- [ ] prepare kaggle submission

### Minor points, idea collection

- [ ] In keras, model.fit(...) returns the history of training and validation losses and metrics over epochs. We should keep this.


## Journal

### Week one, homework

For prediction, we cannot  use the test images directly; instead, we need preprocssing to generate numpy arrays. Keras provides a `predict_generator()` method which should be quite helpful here.

Also, we should look into data augmentation, as provided by the image data generator; this may help to push the accuracy further. 

### 2017-01-25 Week one, homework
I got the p2.large machine up and running, week-one assignments are handled in the corresponding notebook. Finetuning the model took approx. 8 minutes, using a batchsize of 32. Monitoring the GPU revealed that only approx 1GB of RAM was utilized, presumably, I can use a larger batch size.

Result: 
```
Epoch 1/1
20000/20000 [==============================] - 640s - loss: 0.2420 - acc: 0.9543 - val_loss: 0.1680 - val_acc: 0.9743
```

A validation accuracy of 97% looks highly promising to me. We will build on that!


I saved the model using

```
vgg.model.save_weights(path + 'results/2017-01-25-week-one-bs32')
```

