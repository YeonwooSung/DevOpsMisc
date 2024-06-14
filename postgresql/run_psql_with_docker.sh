
# create volume for postgresql data
docker volume create pd_data

# run postgresql container
docker run -d \
    --name postgres \
    -p 5432:5432 \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_DB=postgres \
    -v pd_data:/var/lib/postgresql/data \
    postgres:15.3-bullseye
