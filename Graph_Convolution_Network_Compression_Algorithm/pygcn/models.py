import torch.nn as nn
import torch.nn.functional as F
from pygcn.layers import GraphConvolution
from pygcn.layers import Masked_GraphConvolution

########################################################################

class Masked_GCN(nn.Module):
    def __init__(self, nfeat, nhid, nclass, dropout):
        super(Masked_GCN, self).__init__()

        self.gc1 = Masked_GraphConvolution(nfeat, nhid)
        self.gc2 = Masked_GraphConvolution(nhid, nclass)
        self.dropout = dropout

    def forward(self, x, adj):
        #x = F.leaky_relu(self.gc1(x, adj), inplace=True)
        x = F.relu(self.gc1(x, adj))
        x = F.dropout(x, self.dropout, training=self.training)
        x = self.gc2(x, adj)
        ret = F.log_softmax(x, dim=1)
        return ret

    def set_masks(self, masks):
        # Should be a less manual way to set masks
        # Leave it for the future
        self.gc1.set_mask(masks[0])
        self.gc2.set_mask(masks[1])
        #self.gc1.set_mask(torch.from_numpy(masks[0]))
        #self.gc2.set_mask(torch.from_numpy(masks[1]))

################################################################################

class GCN(nn.Module):
    def __init__(self, nfeat, nhid, nclass, dropout):
        super(GCN, self).__init__()

        self.gc1 = GraphConvolution(nfeat, nhid)
        self.gc2 = GraphConvolution(nhid, nclass)
        self.dropout = dropout

    def forward(self, x, adj):
        x = F.relu(self.gc1(x, adj))
        x = F.dropout(x, self.dropout, training=self.training)
        x = self.gc2(x, adj)
        return F.log_softmax(x, dim=1)

#################################################################################


