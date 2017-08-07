DOCKER_IMAGE="justinbrush702/phylogenetic-tree-demo"

chmod +x dev-tools.sh

function build () {
  echo "Building image..."
  docker build -t $DOCKER_IMAGE .
}

function run () {
  echo "Running image..."
  docker run $DOCKER_IMAGE
}

function iterate () {
  build
  run
}
