/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * write_shared_file.c
 * Copyright (C) 2025 Vladimir Roncevic <elektron.ronca@gmail.com>
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

int write_shared_file(int fd, const char *buffer)
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
        perror("Invalid buffer pointer.");
        return SHARED_FILE_ERROR;
    }

    //////////////////////////////////////////////////////////////////////////
    /// Initializes the lock structure
    struct flock lock = {
        .l_type = F_WRLCK,
        .l_whence = SEEK_SET,
        .l_start = 0,
        .l_len = 0,
        .l_pid = getpid()
    };

    //////////////////////////////////////////////////////////////////////////
    /// Acquires the lock
    int status = file_shared_lock(fd, &lock);

    if (status == 0)
    {
        //////////////////////////////////////////////////////////////////////
        /// Writes the data to the shared file
        size_t len = strlen(buffer);

        ssize_t bytes_written = write(fd, buffer, len);

        if (bytes_written < 0) {
            perror("Error writing to shared file");
            return SHARED_FILE_ERROR;
        }

        fprintf(stderr, "Process %d has written to data file.\n", lock.l_pid);
    }
    else 
    {
        return SHARED_FILE_ERROR;
    }

    //////////////////////////////////////////////////////////////////////////
    /// Releases the lock
    status = file_shared_unlock(fd, &lock);

    if (status < 0)
    {
        return SHARED_FILE_ERROR;
    }

    return SHARED_FILE_SUCCESS;
}
