class CNNet(nn.Module):

    def __init__(self, out = 10):
        super(CNNet, self).__init__()

        self.conv_1 = nn.Conv2d(in_channels = 1, out_channels = 16, kernel_size = 3)
        nn.init.xavier_normal_(self.conv_1.weight, gain = 2**0.5)
        self.conv_2 = nn.Conv2d(in_channels = 16, out_channels = 8, kernel_size = 2)
        nn.init.xavier_normal_(self.conv_2.weight, 2**0.5)
        self.conv_3 = nn.Conv2d(in_channels = 8, out_channels = 8, kernel_size = 3)
        nn.init.xavier_normal_(self.conv_3.weight, 2**0.5)
        self.fc_1 = nn.Linear(in_features = 8*2*2, out_features = 50)
        nn.init.xavier_normal_(self.fc_1.weight, 2**0.5)
        self.fc_2 = nn.Linear(in_features = 50, out_features = out)
        nn.init.xavier_normal_(self.fc_2.weight, 2**0.5) 

        self.pool = nn.MaxPool2d(kernel_size = 2)


    def forward(self, x):

        x = self.get_features(x)
        output = self.fc_2(x)

        return output

    def get_features(self, x):
        x = self.conv_1(x)
        x = nn.ReLU()(self.pool(x))
        b1 = nn.BatchNorm2d(16).to(device)
        x = b1(x)
        d1 = nn.Dropout(0.2).to(device)
        x  = d1(x)

        x = self.conv_2(x)
        x = nn.ReLU()(self.pool(x))
        b2 = nn.BatchNorm2d(8).to(device)
        x = b2(x)
        d2 = nn.Dropout(0.1).to(device)
        x = d2(x)

        x = self.conv_3(x)
        x = nn.ReLU()(self.pool(x))
        b3 = nn.BatchNorm2d(8).to(device)
        x = b3(x)
        d3 = nn.Dropout(0.1).to(device)
        x = d3(x)
        
        x = self.fc_1(x.view(x.size(0), -1))
        x = nn.ReLU()(x)
        d4 = nn.Dropout(0.2).to(device)
        x = d4(x)
        
        return x