/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * read_shared_file.c
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
 *
 * myipc is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * myipc is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */
#include "shared_file.h"

int read_shared_file(int fd, char *buffer)
{
    //////////////////////////////////////////////////////////////////////////
    /// Checks if the shared file descriptor is valid
    if (fd < 0)
    {
        perror("Invalid shared file descriptor.");
        return SHARED_FILE_ERROR;
    }

    //////////////////////////////////////////////////////////////////////////
    /// Checks if the buffer pointer is valid
    if (buffer == NULL)
    {
        perror("Invalid buffer pointer provided.");
        return SHARED_FILE_ERROR;
    }

    //////////////////////////////////////////////////////////////////////////
    /// Initializes the lock structure
    struct flock lock = {
        .l_type = F_RDLCK,
        .l_whence = SEEK_SET,
        .l_start = 0,
        .l_len = 0,
        .l_pid = getpid()
    };

    //////////////////////////////////////////////////////////////////////////
    /// Trys to acquire the read lock
    int status = file_shared_lock(fd, &lock);

    if (status < 0)
    {
        perror("Failed to get a read-only lock.");
        return SHARED_FILE_ERROR;
    }

    //////////////////////////////////////////////////////////////////////////
    /// Reads the data from the shared file
    ssize_t bytes_read = 0;
    ssize_t ret = 0;

    while ((ret = read(fd, buffer, SHARED_FILE_BUFFER_SIZE)) > 0)
    {
        bytes_read += ret;
        buffer += ret;
    }

    fprintf(stderr, "Process %d has read data from file.\n", lock.l_pid);

    //////////////////////////////////////////////////////////////////////////
    /// Releases the lock
    status = file_shared_unlock(fd, &lock);

    if (status < 0)
    {
        perror("Explicit unlocking shared file failed.");
        return SHARED_FILE_ERROR;
    }

    //////////////////////////////////////////////////////////////////////////
    /// In case of failed read, returns -1
    if (ret < 0)
    {
        perror("Failed to read from shared file.");
        return SHARED_FILE_ERROR;
    }

    return bytes_read;
}
