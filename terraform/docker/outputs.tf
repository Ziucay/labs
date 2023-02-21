output "container_id" {
  description = "Docker container id"
  value = docker_container.nginx.id
}

output "container_name" {
  description = "Docker container name"
  value = docker_container.nginx.name
}
