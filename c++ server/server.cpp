#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {
    // Create socket
    int serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket == -1) {
        std::cerr << "Error: Unable to create socket\n";
        return 1;
    }

    // Bind to port 5566
    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY;
    serverAddr.sin_port = htons(5566);
    if (bind(serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == -1) {
        std::cerr << "Error: Unable to bind to port\n";
        close(serverSocket);
        return 1;
    }

    // Listen for incoming connections
    if (listen(serverSocket, 5) == -1) {
        std::cerr << "Error: Unable to listen on socket\n";
        close(serverSocket);
        return 1;
    }

    std::cout << "Server started. Listening on port 5566.\n";

    while (true) {
        // Accept incoming connection
        struct sockaddr_in clientAddr;
        socklen_t clientAddrLen = sizeof(clientAddr);
        int clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &clientAddrLen);
        if (clientSocket == -1) {
            std::cerr << "Error: Unable to accept connection\n";
            close(serverSocket);
            return 1;
        }

        // Send message to client
        std::string message = "I am a C++ server running on port 5566\n";
        if (send(clientSocket, message.c_str(), message.size(), 0) == -1) {
            std::cerr << "Error: Unable to send message\n";
            close(clientSocket);
            close(serverSocket);
            return 1;
        }

        // Close client socket
        close(clientSocket);
    }

    // Close server socket
    close(serverSocket);

    return 0;
}
