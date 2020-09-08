import torch

from scMVP.dataset import GeneExpressionDataset
from scMVP.inference import UnsupervisedTrainer
from scMVP.models import VAE

use_cuda = torch.cuda.is_available()


def unsupervised_training_one_epoch(dataset: GeneExpressionDataset):
    vae = VAE(dataset.nb_genes, dataset.n_batches, dataset.n_labels)
    trainer = UnsupervisedTrainer(vae, dataset, train_size=0.5, use_cuda=use_cuda)
    trainer.train(n_epochs=1)
