#argoCD


https://www.youtube.com/watch?t=1m4s&v=aWDIQMbp1cc&feature=youtu.be

github.com/jesseuen/argocd-examples-apps   # @ 4:44



kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

https://argoproj.github.io/argo-cd/getting_started/

cli install


https://argoproj.github.io/argo-cd/cli_installation/


VERSION=$(curl --silent "https://api.github.com/repos/argoproj/argo-cd/releases/latest" | grep '"tag_name"' | sed -E 's/.*"([^"]+)".*/\1/')

curl -sSL -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/download/$VERSION/argocd-linux-amd64

chmod +x /usr/local/bin/argocd


run
argocd version
# there by by an address error


kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
# fix this so it's a working nodeport?